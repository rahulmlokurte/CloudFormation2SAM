import yaml
import json


def convert_to_sam(cf_file, sam_file):
    with open(cf_file.name, 'r') as f:
        data = yaml.load(f, Loader=yaml.FullLoader)
        sam_template = {
            "Transform": 'AWS::Serverless-2016-10-31',
            "Resources": {}
        }

        for resource_name, resource in data["Resources"].items():
            if resource['Type'] == 'AWS::Events::Rule':
                event_pattern = json.dumps(resource['Properties'].get('EventPattern', {}))
                if event_pattern == '{}':
                    sam_template['Resources'][resource_name] = {
                        "Type": "AWS::Events::Rule",
                        "Properties": {
                            **{k: v for k, v in resource['Properties'].items() if k != 'EventPattern'}
                        }
                    }
                else:
                    sam_template['Resources'][resource_name] = {
                        "Type": "AWS::Events::Rule",
                        "Properties": {
                            "EventPattern": event_pattern,
                            **{k: v for k, v in resource['Properties'].items() if k != 'EventPattern'}
                        }
                    }

    with open(sam_file.name, "w") as file:
        yaml.dump(sam_template, file)

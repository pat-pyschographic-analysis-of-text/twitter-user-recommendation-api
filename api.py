import json, random

def main(event, context):
    score = random.random()

    return {
        "statusCode": 200,        
        "body": json.dumps({ "score": score })
    }

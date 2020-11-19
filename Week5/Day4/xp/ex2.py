import json
sampleJson = """{ 
   "company":{ 
      "employee":{ 
         "name":"emma",
         "payable":{ 
            "salary":7000,
            "bonus":800
         }
      }
   }    
}"""
salary = json.loads(sampleJson)

print(salary["company"]["employee"]["payable"]["salary"])

with open("sample.json", "w") as f:
    json.dump(sampleJson, f)
    
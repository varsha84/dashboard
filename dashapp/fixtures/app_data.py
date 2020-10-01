import json
import random
product_name = ["Android", "iOS", "Windows"]
verdict = ["PASS", "FAIL", "NOT_TESTED"]
def create_product(data):
    for i in range(len(product_name)):
        d = {"fields":{}}
        d["model"] = "dashapp.product"
        d["pk"] = i+1
        d["fields"]["product_id"] = i+1
        d["fields"]["product_name"] = product_name[i]
        data.append(d)
        

def create_testcases(data):
    for i in range(100):
        d = {"fields":{}}
        d["model"] = "dashapp.testcase"
        d["pk"] = i+1
        d["fields"]["test_id"] = i+1
        d["fields"]["title"] = "Test case title for testcase_{}".format(i+1)
        data.append(d)
        
    
def create_release(data):
    j = 1
    for p in product_name:
        for i in range(5):
            d = {"fields":{}}
            d["model"] = "dashapp.release"
            d["pk"] = j 
            d["fields"]["release_id"] = j 
            d["fields"]["release_name"] = "{}_{}".format(p, i+1)
            d["fields"]["product_id"] = product_name.index(p)+1
            j = j+1
            data.append(d)
        
def create_testrun(data):
    j = 1
    for r in range(1, 15):
        for i in range(10):
            d = {"fields":{}}
            d["model"] = "dashapp.testrun"
            d["pk"] = j
            d["fields"]["release_id"] = r
            d["fields"]["test_id"] = i+1
            d["fields"]["test_result"] = random.choice(verdict)     
            j = j+1
            data.append(d)



if __name__ == "__main__":
    data = []
    f = open("app_data.json", "w")
    create_product(data)
    create_testcases(data)
    create_release(data)
    create_testrun(data)
    json.dump(data, f)
    f.close()
    
    
    
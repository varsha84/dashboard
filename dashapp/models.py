from django.db import models

class Product(models.Model):
    product_id = models.CharField(max_length=50)
    product_name = models.CharField(max_length=50)
    def __str__(self):
        return "{}".format(self.product_name)

class Release(models.Model):
    release_id = models.IntegerField()
    release_name = models.CharField(max_length=50)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE) 
    
    
class Testcase(models.Model):
    test_id = models.IntegerField()
    title = models.CharField(max_length=50) 
    
    def __str__(self):
        return "{}".format(self.title)
            
class Testrun(models.Model):
    test_id = models.ForeignKey(Testcase, on_delete=models.CASCADE)
    release_id = models.ForeignKey(Release, on_delete=models.CASCADE)
    test_result = models.CharField(max_length=20)

    def __str__(self):
        return "{}-{}".format(self.test_id.title, self.test_result)  

    
    
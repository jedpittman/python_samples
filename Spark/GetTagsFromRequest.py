
# note this code only handles well formed html/xml documents.
# badly formatted tags like <stuff <innerstuff> would break.
# As would <outer <inner tag> />
def gettag(mystr):
    mylist = []
    l1=mystr.find("<")
    if l1 >= 0:
        l2 = mystr.find(">")
        if l2 >= 0:
            mylist.append(mystr[l1:l2+1])
            res = gettag(mystr[l2+1:])
            if len(res) > 0:
                for w in res:
                    mylist.append(w)
    return mylist

from pyspark.sql import SparkSession
spark = SparkSession.builder.master('local').getOrCreate()
sc = spark.sparkContext

g = requests.get("http://www.google.com")

rdd = sc.parallelize(g.text.split(','))
rdd1 = rdd.filter(lambda b: "<" in b)
rdd1.flatMap(lambda m: gettag(m)).collect()

rdd2 = rdd1.flatMap(lambda m: gettag(m))
rdd2.filter(lambda l: "<meta" in l).repartition(1).saveAsTextFile("metafile")
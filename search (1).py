from drives import *
from multithreading import *
#locating files in drives
def individual(query,filename):
    flag=0
    for d in query:
        drv=d+":\\"
        for root,dirs,files in os.walk(drv):
            for name in files:
                if name==filename:
                    result=(str(os.path.join(root,name)))
                    print(result)
                    flag=1
    return(flag)
d=mydrive()
query=input("enter the drive u want to search in:")
filename=input("enter the filename:")
flag=individual(query,filename)
if flag==0:
    print("file not found:")


# parallel process of searching file in drives
def multiThreading(filename, drives):
    results_ = []
    with concurrent.futures.ThreadPoolExecutor() as Executor:
    # submit method returns the file search update
        results = [Executor.submit(locate_file, filename, drive) for drive in drives]
        for f in concurrent.futures.as_completed(results):
                results_.append(f.result())
    return results_





#1
#python installation
pip --version
python -m ensurepip --upgrade
#numpy and pandas
pip install numpy pandas
python -c "import numpy; print(numpy.__version__)"
python -c "import pandas; print(pandas.__version__)"
#testing numpy and pandas
import numpy as np
import pandas as pd

# Test NumPy
print("NumPy Test:")
array = np.array([10, 20, 30, 40, 50])
print("Array:", array)
print("Array Sum:", array.sum())

# Test Pandas
print("\nPandas Test:")
data = {"Name": ["John", "Doe", "Smith"], "Age": [25, 30, 35]}
df = pd.DataFrame(data)
print("DataFrame:")
print(df)



#2 hadoop
java -version
#set env
export HADOOP_HOME=/path/to/hadoop
export PATH=$PATH:$HADOOP_HOME/bin:$HADOOP_HOME/sbin
export JAVA_HOME=/path/to/java
source ~/.bashrc
hadoop version
#configure hadoop
#edit core-site.xml
<configuration>
  <property>
    <name>fs.defaultFS</name>
    <value>hdfs://localhost:9000</value>
  </property>
</configuration>
#edit hdfs-site.xml
<configuration>
  <property>
    <name>dfs.replication</name>
    <value>1</value>
  </property>
  <property>
    <name>dfs.namenode.name.dir</name>
    <value>file:///path/to/hadoop/namenode</value>
  </property>
  <property>
    <name>dfs.datanode.data.dir</name>
    <value>file:///path/to/hadoop/datanode</value>
  </property>
</configuration>
#edit mapred-site.xml
<configuration>
  <property>
    <name>mapreduce.framework.name</name>
    <value>yarn</value>
  </property>
</configuration>
#Edit yarn-site.xml
<configuration>
  <property>
    <name>yarn.nodemanager.aux-services</name>
    <value>mapreduce_shuffle</value>
  </property>
</configuration>
format hadoop: hdfs namenode -format
start-dfs.sh
start-yarn.sh
hdfs dfs -mkdir /test
hdfs dfs -put local_file.txt /test
hdfs dfs -ls /test
hdfs dfs -cat /test/local_file.txt



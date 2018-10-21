#pre condicoes
- arquivos map.py e reduce.py devem estar dentro de /tmp/data/scripts/ dentro do hadoop
- arquivo de dados votacao_secao_2014_SP.txt  deve estar em /tmp/data/votacao/ dentro do hadoop

#execucao
- $HADOOP_HOME/bin/hadoop jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-3.0.0.jar -input /tmp/data/votacao -output /tmp/data/output -mapper "python /tmp/data/scripts/map_trab3.py" -reducer "python /tmp/data/scripts/reduce_trab3.py"

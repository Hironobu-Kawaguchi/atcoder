#!bash
id=0
for i in  `seq 100`
do
    idx=`printf %04d $id`
    echo $idx
    python3 ahc005_a.py <in/$idx.txt >out/$idx.txt
    # python3 ahc005_a.py <in/$idx.txt
    id=$((id+1))
done

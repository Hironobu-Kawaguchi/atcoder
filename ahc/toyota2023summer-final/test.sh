# !/bin/bash
for N in {0000..0099}; do
    S=$(printf "%04d" "${N}")
    echo $S
    python3 a.py < ./tools/in/$S.txt > ./tools/out/$S.txt
    # cargo run -r --bin vis in/$S.txt out/$S.txt
done

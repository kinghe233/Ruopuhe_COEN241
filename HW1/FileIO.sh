sysbench --threads=8 --test=fileio --file-total-size=1GB prepare 
sysbench --threads=8 --test=fileio --file-total-size=1GB --file-test-mode=rndrw --time=30 --max-requests=0 run 
sysbench --threads=8 --test=fileio --file-total-size=1GB cleanup

sysbench --threads=8 --test=fileio --file-total-size=1GB prepare 
sysbench --threads=8 --test=fileio --file-total-size=1GB --file-test-mode=seqwr --max-time=30 --max-requests=0 run 
sysbench --threads=8 --test=fileio --file-total-size=1GB cleanup

sysbench --threads=8 --test=fileio --file-total-size=1GB prepare 
sysbench --threads=8 --test=fileio --file-total-size=1GB --file-test-mode=rndwr --max-time=30 --max-requests=0 run 
sysbench --threads=8 --test=fileio --file-total-size=1GB cleanup

from redis.sentinel import Sentinel
import time

def monitor_sentinel_cluster():
    """Monitor Sentinel cluster health."""
    sentinel = Sentinel([
        ('sentinel-1', 26379),
        ('sentinel-2', 26379),
        ('sentinel-3', 26379)
    ], password='tsgspasswd')

    while True:
        try:
            # Get master info
            master = sentinel.discover_master('mymaster')
            print(f"Current master: {master[0]}:{master[1]}")

            # Get replica info
            replicas = sentinel.discover_slaves('mymaster')
            print(f"Replicas: {len(replicas)}")
            for replica in replicas:
                print(f"  - {replica[0]}:{replica[1]}")

            # Check master health
            master_conn = sentinel.master_for('mymaster')
            info = master_conn.info('replication')
            print(f"Connected replicas: {info['connected_slaves']}")

        except Exception as e:
            print(f"Error: {e}")

        time.sleep(10)

monitor_sentinel_cluster()
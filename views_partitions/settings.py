
import environs

env = environs.Env()
env.read_env()

DB_HOST = env.str("PARTITIONS_DB_HOST", "127.0.0.1")
DB_PORT = env.int("PARTITIONS_DB_PORT", 5432)
DB_USER = env.str("PARTITIONS_DB_USER", "postgres")
DB_NAME = env.str("PARTITIONS_DB_NAME", "postgres")
DB_SSL = env.str("PARTITIONS_DB_SSL", "allow")
DB_PASSWORD = env.str("PARTITIONS_DB_PASSWORD", None)

LOG_LEVEL = env.str("LOG_LEVEL", "WARNING")

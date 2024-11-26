
kafka_df = (
    spark
    .readStream
    .format("kafka")
    .option("kafka.bootstrap.servers", "ed-kafka:29092")
    .option("subscribe", "device-data")
    .option("startingOffsets", "earliest")
    .load()
)

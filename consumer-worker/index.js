import Kafka from 'node-rdkafka';

const consumer = new Kafka.KafkaConsumer({
  'group.id': 'kafka',
  'metadata.broker.list': 'localhost:9093',
}, {});

consumer.connect();
console.log('Se ejecuta');

consumer.on('ready', () => {
  console.log('consumer ready..')
  consumer.subscribe(['test']);
  consumer.consume();
}).on('data', function(data) {
  console.log(`received message: ${data.value}`);
  // console.log(`received message: ${objectToJson.fromBuffer(data.value)}`);
});
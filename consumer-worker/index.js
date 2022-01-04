import Kafka from 'node-rdkafka';
import objectToJson from './../utils/objectBuffer.js';

const consumer = new Kafka.KafkaConsumer({
  'group.id': 'kafka',
  'metadata.broker.list': 'localhost:9092',
}, {});

consumer.connect();

consumer.on('ready', () => {
  console.log('consumer ready..')
  consumer.subscribe(['test']);
  consumer.consume();
}).on('data', function(data) {
  console.log(`received message: ${objectToJson.fromBuffer(data.value)}`);
});
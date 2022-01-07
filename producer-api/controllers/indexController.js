import Kafka from 'node-rdkafka';
import objectToJson from '../../utils/objectBuffer.js';

const stream = Kafka.Producer.createWriteStream(
  {
    'metadata.broker.list': 'localhost:9092'
  },
  {},
  {
    topic: 'test'
  }
);

stream.on('error', (err) => {
  console.error('Error in our kafka stream');
  console.error(err);
});

function queueRandomMessage(languages) {
  const languagesString = JSON.stringify(languages)
  const success = stream.write(languagesString);
  if (success) {
    console.log(`message queued (${languagesString})`);
  } else {
    console.log('Too many messages in the queue already..');
  }
}

function generateRandomJSON(length = 10) {
  const array = Array.from({ length }, () =>
    Math.floor(Math.random() * length)
  );
  const languages = ['javascript', 'css', 'html', 'ruby', 'java', 'php'];
  const types = ['awesome', 'bad', 'fancy', 'hard'];
  return array.map(()=> {
    return {
      'language': languages[Math.floor(Math.random() * languages.length)],
      'is': types[Math.floor(Math.random() * types.length)]
    };
  });
}

const getIndex = (request, reply) => {
  const randomArrayObjects = generateRandomJSON()
  queueRandomMessage(randomArrayObjects[0]);
  return reply.send({
    json: randomArrayObjects
  });
};

export { getIndex };

import Fastify from 'fastify';
import fastifyCors from 'fastify-cors';
import { routers } from './routers/index.js';

const fastify = Fastify({
  logger: true
});

fastify.register(fastifyCors, {});

fastify.register(routers);

const start = async () => {
  try {
    await fastify.listen(3006);
  } catch (err) {
    process.exit(1);
  }
};
start();

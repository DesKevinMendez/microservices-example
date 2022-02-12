import Fastify from 'fastify';
import fastifyCors from 'fastify-cors';
import { routers } from './routers/index.js';

const hostname = '0.0.0.0';
const port = 3000;

const fastify = Fastify({
  logger: true
});

fastify.register(fastifyCors, {});
fastify.register(routers);

const start = async () => {
  try {
    await fastify.listen(port, hostname);
  } catch (err) {
    process.exit(1);
  }
};
start();
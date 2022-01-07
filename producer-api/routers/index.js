import { getIndex } from "../controllers/indexController.js";

const routers = (fastify, _, done) => {
  fastify.get('/fastify', getIndex);
  done();
};

export { routers };

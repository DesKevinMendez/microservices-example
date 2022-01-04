import { getIndex } from "../controllers/indexController.js";

const routers = (fastify, _, done) => {
  fastify.get('/', getIndex);
  done();
};

export { routers };

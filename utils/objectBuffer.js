import avro from 'avsc';

export default avro.Type.forSchema({
  type: 'record',
  fields: [
    {
      name: 'language',
      type: 'string',
    },
    {
      name: 'is',
      type: 'string',
    }
  ]
});
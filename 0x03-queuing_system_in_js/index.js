import { createClient } from 'redis';

const client = await createClient()
  .on('error', err => console.log('Redis Client Error', err))
  .connect();

await client.set('key', 'value');
const value = await client.get('key');
await client.disconnect();

client.get('framework', function (err, reply) {
  http
    .createServer(function (req, res) {
      res.write('<h1>Hello, Welcome to docker compose</h1>');
      res.write('We will use ' + reply + ' framework');

      res.end();
    })
    .listen(3000);
  console.log(reply);
});
const fs = require('fs');
const path = require('path');

const release = path.join(__dirname, '..', 'build', 'Release');
const nodeFile = path.join(release, 'node_atol_wrapper.node');

if (!fs.existsSync(nodeFile)) {
  process.exit(0);
}

for (const variant of ['dto', 'dto-piot']) {
  const dir = path.join(release, variant);
  if (!fs.existsSync(dir)) {
    continue;
  }
  fs.copyFileSync(nodeFile, path.join(dir, 'node_atol_wrapper.node'));
}

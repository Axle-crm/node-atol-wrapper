const binary = require('@mapbox/node-pre-gyp');
const path = require('path');
const fs = require('fs');

const bindingPath = binary.find(path.resolve(path.join(__dirname, './package.json')));
const cache = Object.create(null);

function toUnpacked(filePath) {
  const asarUnpacked = `${path.sep}app.asar.unpacked${path.sep}`;
  const asar = `${path.sep}app.asar${path.sep}`;
  if (filePath.includes(asarUnpacked)) {
    return filePath;
  }
  return filePath.split(asar).join(asarUnpacked);
}

function copyFileIfMissing(from, to) {
  if (fs.existsSync(to)) {
    return;
  }
  if (to.includes(`${path.sep}app.asar${path.sep}`) && !to.includes(`${path.sep}app.asar.unpacked${path.sep}`)) {
    throw new Error('Cannot write ATOL DTO files into app.asar: ' + to);
  }
  fs.mkdirSync(path.dirname(to), { recursive: true });
  fs.copyFileSync(from, to);
}

function copyDirFiles(fromDir, toDir) {
  if (!fs.existsSync(fromDir)) {
    return;
  }

  fs.mkdirSync(toDir, { recursive: true });
  for (const name of fs.readdirSync(fromDir)) {
    const from = path.join(fromDir, name);
    if (!fs.statSync(from).isFile()) {
      continue;
    }
    copyFileIfMissing(from, path.join(toDir, name));
  }
}

function ensureVariant(variant) {
  const unpackedBinding = toUnpacked(bindingPath);
  const unpackedRelease = path.dirname(unpackedBinding);
  const destDir = path.join(unpackedRelease, variant);
  const destNode = path.join(destDir, path.basename(unpackedBinding));

  const packedRelease = path.dirname(bindingPath);
  const packedVariantDir = path.join(packedRelease, variant);
  const unpackedVariantDir = path.join(unpackedRelease, variant);

  const dllSource = fs.existsSync(path.join(unpackedVariantDir, 'fptr10.dll'))
    ? unpackedVariantDir
    : packedVariantDir;

  if (!fs.existsSync(dllSource)) {
    throw new Error('ATOL DTO variant folder is missing: ' + dllSource);
  }

  if (!fs.existsSync(destNode)) {
    copyDirFiles(dllSource, destDir);
    copyFileIfMissing(unpackedBinding, destNode);
  }
  return destNode;
}

function load(variant) {
  const key = variant === 'dto-piot' ? 'dto-piot' : 'dto';
  if (!cache[key]) {
    cache[key] = require(ensureVariant(key));
  }
  return cache[key];
}

module.exports = { load };

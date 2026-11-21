#!/usr/bin/env python3
# SPDX-License-Identifier: GPL-3.0-or-later
"""sync_waze.py SRC DEST - (and robert/robertn_waze_cluster, the Maps on cluster app, as it is there) native/waze-on-cluster from a checkout of akakingj/myapp-map (SRC, its
native/waze-on-cluster built: build/target/waze-on-cluster) into this repo's DEST, as a tool the Store
installs from a repo tree: every file its component.json installs, committed, and component.json with
no build step, the version and title of native/waze-on-cluster.source.json."""
import json, os, shutil, sys

args = [a for a in sys.argv[1:] if a != '--no-binary']
no_binary = '--no-binary' in sys.argv   # (a first commit before the workflow has built it)
src, dest = os.path.join(args[0], 'native', 'waze-on-cluster'), args[1]
spec = json.load(open(os.path.join(os.path.dirname(dest.rstrip('/')), 'waze-on-cluster.source.json')))
c = json.load(open(os.path.join(src, 'component.json')))
base = c['version']
paths = [f['from'] for f in c['files']] + [u['from'] for u in c['units']] + [d['from'] for d in c.get('dropins', [])]
if os.path.isdir(dest):
    shutil.rmtree(dest)
for p in paths + ['README.md']:
    if no_binary and p == 'build/target/waze-on-cluster':
        continue
    os.makedirs(os.path.join(dest, os.path.dirname(p)), exist_ok=True)
    shutil.copy2(os.path.join(src, p), os.path.join(dest, p))
c.pop('build', None)
c['version'] = spec['version']
c['title'] = spec['title']
c['description'] = ('Waze on cluster %s (robertnisipeanu/idrive-apps) with the map over or under a layout\'s window '
                    '(%s %s), for AK Map Test. Remove Robert\'s Maps on cluster app and tool first.' % (base, spec['repo'], spec['ref']))
open(os.path.join(dest, 'component.json'), 'w').write(json.dumps(c, indent=2) + '\n')
print('waze-on-cluster %s (from %s): %d files' % (spec['version'], base, len(paths)))

# the Maps on cluster app (a source package, built on the unit: mgu-repo.json "build": "unit"), unchanged
app_src = os.path.join(args[0], 'apps', 'robertn_waze_cluster')
app_dest = os.path.join(os.path.dirname(os.path.dirname(dest.rstrip('/'))), 'robert', 'robertn_waze_cluster')
if os.path.isdir(app_dest):
    shutil.rmtree(app_dest)
shutil.copytree(app_src, app_dest, ignore=shutil.ignore_patterns('node_modules', '*.tgz'))
print('robertn_waze_cluster %s' % json.load(open(os.path.join(app_dest, 'mgu-app.json')))['version'])

# 🧠 Fractal Trinity Core Modules

This directory contains the core logic components of the Fractal Trinity Ontology Engine. These modules represent the inner mechanisms of perception, resonance, emergence, and perspective.

Each subdirectory corresponds to a core metaphysical function:

---

## 📁 `monitor/MetaCognitiveMonitor.js`

### Description
Monitors the cognitive and attentional state of the observer (user or AI). Detects drift, energy loss, field distortion, and project stagnation.

### Usage
```js
import { MetaCognitiveMonitor } from './core/monitor/MetaCognitiveMonitor.js';

const monitor = new MetaCognitiveMonitor();
const alerts = await monitor.performCheck();


---

📁 engines/ResonanceCalculator.js

Description

Calculates resonance across semantic, harmonic, and potentially energetic dimensions. Intended to support node-to-node or field-wide similarity metrics.

Usage

import { ResonanceCalculator } from './core/engines/ResonanceCalculator.js';

const calc = new ResonanceCalculator();
const score = await calc.calculateSemanticResonance(nodeA, nodeB);


---

📁 engines/FieldEmergenceEngine.js

Description

Generates emergent "Resonance Fields" from harmonically aligned node clusters. Detects field overlap, narrative cascades, and manages decay.

Usage

import { FieldEmergenceEngine } from './core/engines/FieldEmergenceEngine.js';

const engine = new FieldEmergenceEngine();
const field = engine.detectFieldFormation(clusteredNodes);


---

📁 observer/PerspectiveSystem.js

Description

Encapsulates observer perspective logic. Allows viewpoint switching, filtering, and perceptual styling of the node environment.

Usage

import { PerspectiveSystem } from './core/observer/PerspectiveSystem.js';

const perspectives = {
  cosmic: {
    nodeFilter: (n) => n.type !== 'noise',
    scaleMultiplier: 1.2,
    colorScheme: 'neon-glow'
  }
};

const system = new PerspectiveSystem(perspectives);
system.switchTo('cosmic');


---

🌐 Architecture Notes

All modules use modern ES6 class syntax

Designed for tree-shakable bundling

Can be used in CLI, UI, or server-side contexts



---

📌 TODOs

[ ] Add unit tests (/tests/core/)

[ ] Implement embedding + cosine logic in ResonanceCalculator

[ ] Real-time field emergence visualizer

[ ] Perspective interpolation system



---

🌀 Fractal awareness begins at the core.

---

Would you like me to place this into the `.zip` for download as well?


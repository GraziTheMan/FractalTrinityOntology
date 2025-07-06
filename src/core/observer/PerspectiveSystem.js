// PerspectiveSystem.js
// Manages the observer's perspective filters and dynamic viewpoint logic.

export class PerspectiveSystem {
  constructor(perspectives = {}) {
    this.perspectives = perspectives;
    this.current = null;
  }

  switchTo(perspectiveName) {
    if (this.perspectives[perspectiveName]) {
      this.current = perspectiveName;
      this.transitionEffect(perspectiveName);
    }
  }

  applyToNode(node) {
    const perspective = this.perspectives[this.current];
    if (perspective?.nodeFilter) return perspective.nodeFilter(node);
    return node;
  }

  transitionEffect(perspectiveName) {
    // TODO: Optional visual/audio cue
  }

  getCurrentPerspective() {
    return this.perspectives[this.current];
  }
}
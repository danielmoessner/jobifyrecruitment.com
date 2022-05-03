import Alpine from './alpine/module.esm.js'

window.Alpine = Alpine

Alpine.start()

import './tailwindui/main.js'

document.documentElement.style.setProperty('--scrollbar-width', (window.innerWidth - document.documentElement.clientWidth) + "px");

import Vue from 'vue'
import App from './App.vue'
import ckEditor from './ckEditor.vue'

// eslint-disable-next-line no-new
new Vue({
    el: '#app',
    render: h => h(App)
});

new Vue({ // eslint-disable-line no-new
    el: '#ckEditor',
    render: h => h(ckEditor)
});

import Vue from 'vue'
import App from './App.vue'
import ckEditor from './ckEditor.vue'

// 以下的eslint-disable-line注释是为了禁止ESLint进行检测的，因为在js中，new一个对象必须将该对象赋值给一个变量，
// 而vue的实例化是不需要的，因此为了避免报错(实际没错)添加了该注解

// eslint-disable-next-line no-new
new Vue({
    el: '#app',
    render: h => h(App)
});

new Vue({ // eslint-disable-line no-new
    el: '#ckEditor',
    render: h => h(ckEditor)
});

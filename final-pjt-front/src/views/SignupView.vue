<template>
  <div class="login-view">
    <div class="wrapper">
      <div class="wrapper__logo">
        무비피커
      </div>
      <SignupForm/>
    </div>
  </div>
</template>

<script>
import SignupForm from '../components/SignupForm.vue'

export default {
  name: 'LoginView',
  components: {
    SignupForm
  },

  data() {
    return {
      
    };
  },

  mounted() {
    
  },

  methods: {
    
  },
};
</script>

<style lang="scss" scoped>
@import '../assets/scss/LoginView.scss';
</style>
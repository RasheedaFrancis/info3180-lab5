<template>

<div v-if="msg">
    <div v-if="msg.errors" class="alert alert-danger" role="alert">
        <li v-for="err in msg.errors"> {{ err }} </li>
    </div>
    <div v-else class="alert alert-success" role="alert">
        <p>{{ msg.message }}</p>
    </div>
</div>
  <form @submit.prevent="saveMovie" id="movieForm">
   
    <div class="form-group mb-3">
      <label for="title" class="form-label"> Movie Title</label> 
      <input type="text" v-model="title" name="title" id="title" class="form-control"  />
    </div>
    <div class="form-group mb-3">
      <label for="description" class="form-label">Description</label>
      <textarea v-model="description" name="description" id="description" class="form-control"></textarea>
    </div>
    <div class="form-group mb-3">
      <label for="poster" class="form-label">Movie Poster</label>
      <input type="file" name="poster" id="poster" class="form-control" />
    </div>
    <button type="submit" class="btn btn-primary">Submit</button>
  </form>
</template>


<style>
.form-group , .btn-primary {
    margin-left: 40px;
}
.form-control{
  width: 630px;
}
#description{
  height: 150px;
}
</style>

<script setup>
  import { ref, onMounted } from "vue";

  onMounted(() =>{
      getCsrfToken();
  });
  
  const msg = ref(null);
  let csrf_token = ref("");

  function getCsrfToken() {
      fetch('/api/v1/csrf-token')
      .then((response) => response.json())
      .then((data) => {
          console.log(data);
          csrf_token.value = data.csrf_token;
      })
  }

  function saveMovie() {
      let movieForm = document.getElementById('movieForm');
      let form_data = new FormData(movieForm);

      fetch("/api/v1/movies", {
      method: 'POST',
      body: form_data,
      headers: {
          'X-CSRFToken': csrf_token.value
      }
      }) 
      .then(function (response) { 
          return response.json(); 
      })
      .then(function (data) { 
          console.log(data);
          msg.value = data;
      })
      .catch(function (error) { 
          console.log(error); 
      });
    }
</script>


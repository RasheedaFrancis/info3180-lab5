
 <template>
  <h1>Movies</h1>
  <div class="MovieList">
    <div v-for="movie in movies.movies" class="Movies" style="width: calc(50% - 35px);">
      <img :src="movie.poster" alt="Movie Image" class="MovieImages"  >
      <div class="MovieInfo">
        <h4 class="Movie-title">{{ movie.title }} </h4>
        <p class="Movie-text">{{ movie.description }}</p>
      </div>
    </div>
  </div>
</template>
 
<style>
.MovieList {
  margin-left: 110px;
  margin-right: 90px;
  display: flex;
  flex-wrap: wrap;
  justify-content: space-between;
}

h1 {
  margin-left: 110px;
  margin-bottom: 20px;
}

.MovieImages {
  width: 16em;
  height: 350px;
  object-fit: cover;
}

.Movies {
  display: flex;
  flex-direction: row; 
  margin-bottom: 20px;
  border: 1px solid #ccc; 
}

.MovieInfo {
  padding: 10px;
}

.Movie-title {
  margin-top: 0;
  margin-bottom: 10px;
}

.Movie-text {
  margin-top: 0;
}
</style>

<script setup>
  import { ref, onMounted } from "vue";

  onMounted(() =>{
      fetchMovies();
  });

  const movies = ref([]);

  function fetchMovies() {
      fetch("/api/v1/movies", {
      method: 'GET',
      }) 
      .then(function (response) { 
          return response.json(); 
      })
      .then(function (data) { 
          console.log(data);
          movies.value = data;
          console.log(movies.value);
      })
      .catch(function (error) { 
          console.log(error); 
      });
  }
</script>
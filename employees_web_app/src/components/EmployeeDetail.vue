<template>
  <v-card rounded="xl">
    <v-card-title><h2>{{ name }}</h2></v-card-title>
  </v-card>
</template>

<script>
export default {
  name: "EmployeeDetail.vue",
  props:{
    id: String,
    name: String,
    lastName: String,
    startDate: String,
    birthday: String,
    position: String
  }
}
</script>

<style scoped>

</style>

<template>
  <v-app class="my-3 mx-3">
    <v-row>
      <v-col cols="5">
        <Employees/>
      </v-col>
      <v-col>
        <v-card>
          <v-card-title>Detalle empleados</v-card-title>
        </v-card>
      </v-col>
    </v-row>
  </v-app>
</template>

<script>
  import Employees from "../components/Employees";
  export default {
    name: 'Home',

    components: {
      Employees
    },
  }
</script>

<style>

</style>

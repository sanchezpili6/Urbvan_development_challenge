<template>
  <v-app>
    <v-row>
      <v-col cols="4">
        <v-card>
          <v-card-title>Tabla de empleados</v-card-title>
          <v-card-text>
            <v-data-table>

            </v-data-table>
          </v-card-text>
        </v-card>
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

  export default {
    name: 'Home',

    components: {
    },
  }
</script>

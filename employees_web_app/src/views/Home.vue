<template>
  <v-app class="my-3 mx-3">
    <v-row>
      <v-col cols="5">
        <Employees v-on:childToParent="onPatientClick"/>
      </v-col>
      <v-col>
        <EmployeeDetail :id="id" :name="name" :lastName="lastName" :startDate="startDate" :birthday="birthday" :position="position" :pronouns="pronouns"/>
      </v-col>
    </v-row>
    <v-btn rounded fab fixed bottom right large class="primary" @click="$emit('modal')">
      <v-icon size="55" color="white">mdi-plus</v-icon>
    </v-btn>
  </v-app>
</template>

<script>
  import Employees from "../components/Employees";
  import EmployeeDetail from "../components/EmployeeDetail";
  export default {
    name: 'Home',

    components: {
      Employees,
      EmployeeDetail
    },
    data: () => ({
      id: '',
      name: '',
      lastName:'',
      startDate:'',
      birthday:'',
      position:'',
      pronouns: ''
    }),
    methods:{
      onPatientClick(id, name, lastName, startDate, birthday, position, pronouns){
        this.id=id;
        this.name=name;
        this.lastName=lastName;
        this.startDate=startDate;
        this.birthday=birthday;
        this.position=position;
        this.pronouns=pronouns;
      }
    }
  }
</script>

<style>

</style>

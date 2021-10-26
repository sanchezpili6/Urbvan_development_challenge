<template>
  <v-app class="my-3 mx-3">
    <v-row>
      <v-col>
        <Employees/>
      </v-col>
    </v-row>
    <AddEmployee/>
  </v-app>
</template>

<script>
  import Employees from "../components/Employees";
  import AddEmployee from "../components/AddEmployee";
  export default {
    name: 'Home',

    components: {
      Employees,
      AddEmployee
    },
    data: () => ({
      id: '',
      rfc:'',
      name: '',
      last_name:'',
      start_date:'',
      birthday:'',
      job_position:'',
      pronouns: ''
    }),
    methods:{
      onPatientClick(id, rfc, name, last_name, start_date, birthday, job_position, pronouns){
        this.id=id;
        this.rfc=rfc;
        this.name=name;
        this.last_name=last_name;
        this.start_date=start_date;
        this.birthday=birthday;
        this.job_position=job_position;
        this.pronouns=pronouns;
      }
    }
  }
</script>

<style>

</style>

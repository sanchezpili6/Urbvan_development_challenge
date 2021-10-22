<template>
  <v-container>
    <v-btn
        fab
        color="primary"
        dark
        fixed
        bottom
        right
        class="add"
        @click="overlay=!overlay"
    >
      <v-icon size="50px">mdi-plus</v-icon>
    </v-btn>

    <v-overlay :value="overlay" z-index=  "1">
      <v-card
          elevation="2"
          rounded="xl"
          color="primary"
          height="700"
          width="900"
      >
        <v-card-title justify="center">
          <v-spacer></v-spacer>
          <h1 style="font-size: 40px">CREAR NUEVO EMPLEADO</h1>
          <v-spacer></v-spacer>
          <v-btn fab color="white" small @click="overlay=!overlay"><v-icon color="accent">mdi-close-thick</v-icon></v-btn>
        </v-card-title>
        <v-container></v-container>
        <v-card-text>
            <validation-observer
                ref="observer"
                v-slot="{ invalid }"
            >
              <form @submit.prevent="submit">
                <validation-provider
                    v-slot="{ errors }"
                    name="Name"
                    rules="required|max:10"
                >
                  <v-text-field
                      v-model="name"
                      label="Nombres"
                      required
                  ></v-text-field>
                </validation-provider>
                <validation-provider
                    v-slot="{ errors }"
                    name="lastNames"
                    rules="required|max:10"
                >
                  <v-text-field
                      v-model="lastNames"
                      label="Apellidos"
                      required
                  ></v-text-field>
                </validation-provider>
                <validation-provider
                    v-slot="{ errors }"
                    name="Position"
                    rules="required|max:10"
                >
                  <v-text-field
                      v-model="position"
                      label="Puesto"
                      required
                  ></v-text-field>
                </validation-provider>
                <validation-provider
                    v-slot="{ errors }"
                    name="pronouns"
                    rules="required"
                >
                  <v-select
                      v-model="select"
                      :items="pronouns"
                      :error-messages="errors"
                      label="Pronombre"
                      data-vv-name="select"
                      required
                  ></v-select>
                </validation-provider>
                <v-menu
                    ref="menu"
                    v-model="menu"
                    :close-on-content-click="false"
                    transition="scale-transition"
                    offset-y
                    min-width="auto"
                >
                  <template v-slot:activator="{ on, attrs }">
                    <v-text-field
                        v-model="startDate"
                        label="Fecha de ingreso"
                        prepend-icon="mdi-calendar"
                        readonly
                        v-bind="attrs"
                        v-on="on"
                    ></v-text-field>
                  </template>
                  <v-date-picker
                      v-model="startDate"
                      :max="(new Date(Date.now() - (new Date()).getTimezoneOffset() * 60000)).toISOString().substr(0, 10)"
                      min="2016-01-01"
                      @change="save"
                  ></v-date-picker>
                </v-menu>
                <v-menu
                    ref="menu"
                    :close-on-content-click="false"
                    transition="scale-transition"
                    offset-y
                    min-width="auto"
                >
                  <template v-slot:activator="{ on, attrs }">
                    <v-text-field
                        v-model="birthday"
                        label="Cumpleaños"
                        prepend-icon="mdi-calendar"
                        readonly
                        v-bind="attrs"
                        v-on="on"
                    ></v-text-field>
                  </template>
                  <v-date-picker
                      v-model="birthday"
                      :max="(new Date(Date.now() - (new Date()).getTimezoneOffset() * 60000)).toISOString().substr(0, 10)"
                      min="1950-01-01"
                      @change="save"
                  ></v-date-picker>
                </v-menu>

                <v-row>
                  <v-spacer></v-spacer>
                  <v-btn
                      class="mr-4 accent text--text"
                      type="submit"
                  >
                    submit
                  </v-btn>
                </v-row>
              </form>
            </validation-observer>
        </v-card-text>
      </v-card>
    </v-overlay>
  </v-container>
</template>

<script>
import { required, digits, email, max, regex } from 'vee-validate/dist/rules'
import { extend, ValidationObserver, ValidationProvider, setInteractionMode } from 'vee-validate'

setInteractionMode('eager')

extend('digits', {
  ...digits,
  message: '{_field_} needs to be {length} digits. ({_value_})',
})

extend('required', {
  ...required,
  message: '{_field_} can not be empty',
})

extend('max', {
  ...max,
  message: '{_field_} may not be greater than {length} characters',
})

extend('regex', {
  ...regex,
  message: '{_field_} {_value_} does not match {regex}',
})

export default {
  name: "AddEmployee",
  components: {
    ValidationProvider,
    ValidationObserver,
  },
  data: () =>({
    overlay: false,
    name: '',
    lastNames: '',
    startDate: '',
    birthday: '',
    position: '',
    pronouns: [
      'Ella',
      'Elle',
      'Él'
    ],
    select: null,
    checkbox: null,
  }),
  methods: {
    onButtonClick() {
      window.addEventListener('focus', () => {
      }, { once: true })
    },
    submit () {
      this.$refs.observer.validate()
      this.overlay = false
      this.clear()
    },
    clear(){
      this.name =  '';
      this.lastNames = '';
      this.startDate = '';
      this.birthday = '';
      this.position = '';
      this.select = null;
    }
  },
}
</script>

<style scoped>

</style>

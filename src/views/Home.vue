<template lang="pug">
  v-container.primary(fill-height fluid justify-center)
    v-layout(justify-center align-center column)
      v-flex(shrink)
        h1.headlinefont-weight-medium Choose any local Indonesian song and you'll get the genre :)
      v-flex.ma-3(shrink)
        v-btn.text-capitalize(
          :loading="loading"
          label=".mp3 file"
          @click="filePicked"
          color="info"
        ) Upload a Song!
          v-icon(right) music_note
        input(type="file" ref="picker" style="display:none" accept="audio/mp3" @change="onFilePicked")
      v-flex.ma-3(shrink v-if="isPredicted")
        p.title.mb-1 Musik anda bergenre
        span.red--text.display-1.font-weight-black {{genre}}
      
</template>
<script>
import axios from "axios";
import { BACKEND_HOST } from "@/config";
export default {
  data() {
    return {
      filename: "",
      loading: false,
      genre: ""
    };
  },
  computed: {
    isPredicted() {
      return this.genre != "";
    }
  },
  methods: {
    filePicked() {
      this.$refs.picker.click();
    },
    onFilePicked(e) {
      const files = e.target.files;
      if (files[0] !== undefined) {
        this.filename = files[0].name;
        if (this.filename.lastIndexOf(".") <= 0) {
          return;
        }
        var formData = new FormData();
        formData.append("file", files[0]);
        this.loading = true;
        axios
          .post(BACKEND_HOST + "/predict", formData, {
            header: {
              "Content-Type": "application/x-www-form-urlencoded"
            }
          })
          .then(r => {
            this.genre = r.data.genre;
            this.loading = false;
          });
      }
    }
  }
};
</script>

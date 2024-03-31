/** @type {import('tailwindcss').Config} */
const colors = require('tailwindcss/colors')

module.exports = {
   content: ["./src/**/*.{html,js}"],
   theme: {
    extend: {
        colors: {
        'red1': '#dc2626',
        'red2': '#ef4444',
        'red3': '#f87171',
        'red4': '#fca5a5',
        'red5': '#fecaca',
        'red6': '#fee2e2',
        'red7': '#fef2f2',
        'blue': '#1fb6ff',
        'mycolorpurple': '#7e5bef',
        'pink': '#ff49db',
        'mycolororange': '#ff7849',
        'cgreen': '#13ce66',
        'mycoloryellow': '#ffc82c',
        'gray-dark': '#273444',
        'gray': '#8492a6',
        'gray-light': '#d3dce6',
        'green1' : '#84cc16',
        'green2' : '#d9f99d',
        'light-blue': colors.sky,
        cyan: colors.cyan,
      },
      gridTemplateAreas: {
        'layout': [
          'header header header header header header',
          'menu main main main right right',
          'menu footer footer footer footer footer',
        ],
      },
    },
  },
  variants: {},
  plugins: [],
}


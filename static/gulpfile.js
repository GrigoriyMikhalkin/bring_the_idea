var gulp = require("gulp");
var minifyCSS = require("gulp-minify-css");
var uglify = require("gulp-uglify");

gulp.task("minify-css", function() {
	return gulp.src(__dirname+"/css/*.css")
		.pipe(minifyCSS())
		.pipe(gulp.dest(__dirname+"/build/css/"))
});

gulp.task("uglify", function() {
	 return gulp.src(__dirname+"/js/*.js")
                .pipe(uglify())
                .pipe(gulp.dest(__dirname+"/build/js/"))

});

gulp.task("minify", ["minify-css", "uglify"]);

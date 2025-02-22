// 定义自定义INI模式
CodeMirror.defineMode("customIni", function() {
  return {
    token: function(stream, state) {
      if (stream.sol() && stream.match(/^\[.*?\]$/)) {
        return "ini-section"; // 自定义节名称样式
      }
      if (stream.match(/^[a-zA-Z0-9_.-]+(?=\s*=)/)) {
        return "ini-variable"; // 自定义变量名样式
      }
      if (stream.match("=")) {
        return "ini-equals"; // 自定义等号样式
      }
      if (stream.match(/^[^[\]=]+$/)) {
        return "ini-value"; // 自定义值的样式
      }
      stream.next();
      return null;
    }
  };
});
CodeMirror.defineMIME("text/x-custom-ini", "customIni");


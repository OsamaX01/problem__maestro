document.addEventListener("DOMContentLoaded", function() {
    var editor = CodeMirror.fromTextArea(document.getElementById('code-editor'), { 
        mode: "text/x-csrc",
        theme: "monokai",
        lineNumbers: true,
        matchBrackets: true,
        autoCloseBrackets: true,
        lineWrapping: true,
        viewportMargin: Infinity,
        styleActiveLine: true,
    });
    editor.setSize(null, "25em");

    
    var defaultCode = `#include<iostream>

using namespace std;

int main() {

}`;
    editor.setValue(defaultCode);

    document.getElementById('snippet-form').addEventListener('submit', function() {
        document.getElementById('code-editor').value = editor.getValue();
    });
});
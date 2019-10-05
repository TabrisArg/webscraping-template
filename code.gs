function myFunction() {
    var ss = SpreadsheetApp.getActiveSpreadsheet();
    var sheet = ss.getSheets()[0];
    // Passing only two arguments returns a "range" with a single cell.
    var range = sheet.getRange(1, 4);
    var values = range.getValues();
    for (let i = 0; index < array.length; index++) {
        const element = array[index];
        
    }
    Logger.log(values);
    }
    
    
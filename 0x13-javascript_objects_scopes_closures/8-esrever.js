exports.esrever = function (list) {
    const reversedList = [];
    
    list.forEach((element) => {
      reversedList.unshift(element);
    });
    
    return reversedList;
  };
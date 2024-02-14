#!/usr/bin/node

exports.esrever = function (list) {
  const len = list.length - 1;

  for (let i = 0; i < len / 2; i++) {
    const temp = list[i];
    list[i] = list[len - i];
    list[len - i] = temp;
  }
  return list;
};

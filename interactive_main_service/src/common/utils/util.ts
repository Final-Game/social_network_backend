import moment from 'moment';

export const isEmpty = (value: any): boolean => {
  if (value === null) {
    return true;
  } else if (typeof value !== 'number' && value === '') {
    return true;
  } else if (value === 'undefined' || value === undefined) {
    return true;
  } else if (value !== null && typeof value === 'object' && !Object.keys(value).length) {
    return true;
  } else {
    return false;
  }
};

export const dateToString = (value: Date): string => {
  return (value && moment(value).format('YYYY-MM-DD')) || null;
};

export const stringToDate = (value: string): Date => {
  return (value && new Date(value)) || null;
};

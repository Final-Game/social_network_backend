export enum Gender {
  MALE = 0,
  FEMALE,
  UN_KNOWN,
}

export function getGender(_str: string): number | null {
  const keys = Object.keys(Gender);
  const idx: number = keys.indexOf(_str);
  if (idx < 0) {
    return null;
  }

  return (keys[keys.indexOf(_str) - keys.length / 2] as unknown) as number;
}

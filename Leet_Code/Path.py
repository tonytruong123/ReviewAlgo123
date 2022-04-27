def shortenPath(absolutePath):
  res = [a.strip() for a in absolutePath.split("/") if a]
  print(res)
  ans_list = []

  for path in res:
    if path != ".." and path != ".":
      ans_list.append(path)
    elif path == ".":
      continue
    else:
      if ans_list:
        ans_list.pop()
  if ans_list:
    return "/" + "/".join(ans_list) + "/"
  return "/" + "/".join(ans_list)

print(shortenPath("/etc/../../apache2/original/.extra/.."))
print(shortenPath("/"))
print(shortenPath("/ User Data /"))
print(shortenPath(("/")))
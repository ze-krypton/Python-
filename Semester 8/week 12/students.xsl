<?xml version="1.0" encoding="UTF-8"?>

<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform" version="1.0">

<xsl:template match="/">
<html>
<head>
<title>Student Table</title>

<style>
table {
  border-collapse: collapse;
  margin: auto;
  font-family: Arial;
}

th {
  background-color: #3498db;
  color: white;
  padding: 10px;
}

td {
  padding: 10px;
  text-align: center;
}

tr:nth-child(even) {
  background-color: #f2f2f2;
}
</style>

</head>

<body>

<h2 style="text-align:center;">Student Details</h2>

<table border="1">
<tr>
<th>Name</th>
<th>Course</th>
<th>Marks</th>
</tr>

<xsl:for-each select="students/student">
<tr>
<td><xsl:value-of select="name"/></td>
<td><xsl:value-of select="course"/></td>
<td><xsl:value-of select="marks"/></td>
</tr>
</xsl:for-each>

</table>

</body>
</html>
</xsl:template>

</xsl:stylesheet>